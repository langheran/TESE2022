# Taller de Aprendizaje Automático en GCP con BigQuery
<h4>Congreso Nacional de Proyectos de Investigación e Innovación Tecnológica y Robótica 2022</h4>

[![NDS](https://github.com/langheran/TESE2022/raw/main/images/nds.png)](https://ndscognitivelabs.com/) <a href="https://www.facebook.com/SMITEIMYT"><img src="https://github.com/langheran/TESE2022/raw/main/images/logo.png" width="200"></a>

![GitHub last commit](https://img.shields.io/github/last-commit/langheran/TESE2022) [![Repo Size](https://img.shields.io/github/repo-size/langheran/TESE2022.svg)](https://github.com/langheran/TESE2022/README.md)
-----------------

## Agenda

| Tiempo  | Contenido                                                                                                                                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 45 mins | [0. Introducción al desarrollo de paquetes en Python](./paquete_python/README.md)                                                                                                                       |
| 30 mins | [1. Introducción a BigQuery](https://docs.google.com/presentation/d/e/2PACX-1vQtHHDqQQltagK2XLVUPHEtTO5p0R-gU6MmWScdarflz9z4V8GfYV40vg1sq6Gps4s5nZ_iLFJxV-rl/embed?start=false&loop=false&delayms=3000) |
| 40 mins | [2. Taller BigQuery](taller.ipynb)                                                                                                                                                                      |
| 30 mins | [3. Hacer un microservicio en flask para predicción](./api/README.md)                                                                                                                                   |
| 10 mins | 4. Preguntas                                                                                                                                                                                            |

## 1. Introducción a BigQuery

[![Google](https://img.shields.io/badge/Google%20Slides-FBBC04?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAP1BMVEUAAAD%2FvwD1tAD1tQD0tQD0tAD1tAD0tQD%2FtgD0twD0tAD0tQD3twD1tAD1tQD4tAD%2FuwD1tgD1tQD0tAD%2F%2F%2F97fnsdAAAAE3RSTlMAEHvL8O%2FJeA5H7OpD%2FPtED3rKY%2F8p%2FQAAAG5JREFUWMPt17kRgEAQA8EBjv9nyT9WDCLg5AAlBdC2BqAoqxSPVzdtBwD9EJkbJ4B%2BjuwtK2xDCBs79pDWcmhAQ9KARIgzYOBdwPl4BgwYMGDAwL8B%2FwMDXwfk5JGjS84%2BOTzl9NXjOzf%2F053%2FF9bUMa%2FoE83%2BAAAAAElFTkSuQmCC)](https://docs.google.com/presentation/d/e/2PACX-1vTPQrYItMMV-KMaIRf0LxL5qYlmfbatFZIZhc5qybJKjtnZdF57YXHFGePYHOswAzbywA627So6Au6a/pub?start=false&loop=false&delayms=3000)

## 2. Taller BigQuery

Para este taller necesitas crear primero una [cuenta](http://support.google.com/mail/answer/56256?hl=en) gratuita de Google o accesar con la tuya. Eso lo puedes hacer [aquí](http://support.google.com/mail/answer/56256?hl=en). 

Con la nueva cuenta que creamos, abrir el modo incognito de chrome accesar a http://google.com/account para loguearnos.

Luego abrimos este link ahí para entrar a Cloud Shell.

[![Abrir en Cloud Shell](http://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/langheran/TESE2022&tutorial=tutorial.md&cloudshell_git_branch=main&ephemeral=true)

Al abrir la ventana del `Cloud Shell` hacer click en `Trust repo` y seguir el tutorial que se abre. 

<img src="https://github.com/langheran/TESE2022/raw/main/images/trust_repo.png" data-canonical-src="https://github.com/langheran/TESE2022/raw/main/images/trust_repo.png" width="500" />

Dado que en modo incognito las cookies están deshabilitadas, abrimos el editor en una nueva ventana.

![nueva_ventana](https://github.com/langheran/TESE2022/raw/main/images/nueva_ventana.png)
