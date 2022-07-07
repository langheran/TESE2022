# %%
import json
import os
from dotenv import load_dotenv, find_dotenv

DOTENV = os.environ.get('DOTENV', find_dotenv())
load_dotenv(DOTENV, override=True)

from flask import (
  Flask,
  render_template,
  jsonify,
  request
)

from google.oauth2 import service_account
from google.cloud import bigquery

# %%
credentials_file = 'google-credentials.json'
json_str = os.environ.get('GOOGLE_CREDENTIALS')
json_data = json.loads(json_str)
json_data['private_key'] = json_data['private_key'].replace('\\n', '\n')
json_filepath = credentials_file
if not os.path.exists(json_filepath):
    with open(json_filepath, 'w', encoding='utf-8') as fp:
        json.dump(json_data, fp, indent=4, ensure_ascii=False)
# %%
GCP_PROJECT = os.environ.get('GCP_PROJECT')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file

# %%
credentials = service_account.Credentials.from_service_account_file(
    credentials_file,
)
bq_client = bigquery.Client(
    credentials = credentials,
    project=GCP_PROJECT
)

# sql = "SELECT * from publicdata.samples.natality LIMIT 10"
# bq_client.query(sql).to_dataframe()

# %%

app = Flask(__name__)

@app.route('/')
def index():
  if request.is_json:
    obj = request.json or {}
    sql = f'''
    SELECT
      *
    FROM
      ml.PREDICT(MODEL demo.babyweight_model_asis,
          (SELECT
              '{bool(obj['is_male'])}' AS is_male,
              {obj['mother_age']} AS mother_age,
              '{obj['plurality']}' AS plurality,
              {obj['gestation_weeks']} AS gestation_weeks
        ))
    '''
    result = bq_client.query(sql).to_dataframe().to_dict('records')[0]
    return jsonify(result), 200

if __name__ == '__main__':
  app.run(debug=True)
