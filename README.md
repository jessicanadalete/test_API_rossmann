# [English] Rossmann - Sales Prediction API

This repository contains the API developed to provide sales forecasts for the Rossmann drugstore chain. The API was created to serve predictions generated from a trained machine-learning model developed in the main project. The API is hosted on the Render platform and consumed by a Telegram bot, allowing for quick sales forecast queries for Rossmann stores.

## Objective

The API objective is to provide sales predictions for Rossmann stores based on a predictive model that considers factors such as promotions, holidays, competition, and seasonality. The API enables Rossmann managers and the CFO to make real-time strategic decisions about store operations, such as investing in renovations.

## Features

The API offers the following features:

- Receive a POST request with store data (such as the store ID) and return the sales forecast for the next 6 weeks.
- Integrate with the Telegram bot, allowing users to get forecasts by sending the store code.

## Endpoints

POST /rossmann/predict
This endpoint receives input data (store ID) and returns the sales forecast for that store. The basic workflow is as follows:

1. The user provides the ID of a specific store.
2. The API calls the trained predictive model, passing the store data as input.
3. The sales forecast for the next 6 weeks is returned as a response.

## Requirements

- Python 3.8+
- Flask
- Pandas
- Scikit-learn
- Requests

## Deployment on Render

The API is configured to be deployed on the Render platform. The deployment setup uses environment variables and necessary files to host the application.

## Repository Structure

- model/: the trained model used by the API to generate sales forecasts.
- requirements.txt: The list of project dependencies.
- Procfile: commands executed during application deployment (in this case, used by Render to start the Flask application).
- Rossmann/: Rossmann class, which is responsible for encapsulating all the data processing logic, including cleaning, feature engineering, and generating predictions.
- Parameter/: auxiliary and configurable parameters used in sales forecastings, such as seasonality information, holidays, and competition details.
- handler/: contains the code that handles API requests, input data processes and integrates with the machine learning model to generate predictions.


# [Portuguese] Rossmann - API de Previsão de Vendas

Este repositório contém a API desenvolvida para fornecer previsões de vendas da rede de farmácias Rossmann. A API foi criada para servir previsões geradas a partir de um modelo de machine learning treinado, que foi desenvolvido no projeto principal. A API está hospedada na plataforma Render e é consumida por um bot do Telegram, permitindo consultas rápidas de previsão de vendas das lojas Rossmann.

## Objetivo

O objetivo desta API é disponibilizar previsões de vendas para as lojas da Rossmann, com base em um modelo preditivo que considera fatores como promoções, feriados, competição, e sazonalidade. A API possibilita que os gestores e o CFO da Rossmann tomem decisões estratégicas em tempo real sobre a operação das lojas, como o investimento em reformas.

## Funcionalidades

A API oferece as seguintes funcionalidades:

- Receber um POST com os dados da loja (como o ID da loja) e devolver a previsão de vendas para as próximas 6 semanas.
- Integrar com o bot do Telegram, permitindo que os usuários obtenham previsões enviando o código da loja.

## Endpoints

POST /rossmann/predict
Este endpoint recebe os dados de entrada (ID da loja) e retorna a previsão de vendas para essa loja. O fluxo de trabalho básico é o seguinte:

1. O usuário fornece o ID de uma loja específica.
2. A API faz a chamada ao modelo preditivo treinado, passando os dados da loja como entrada.
3. A previsão de vendas para as próximas 6 semanas é retornada como resposta.

## Requisitos

- Python 3.8+
- Flask
- Pandas
- Scikit-learn
- Requests

## Deploy na Render

A API está configurada para ser implantada na plataforma Render. A configuração do deploy utiliza as variáveis de ambiente e arquivos necessários para hospedar a aplicação.

## Estrutura do Repositório

- model/: O arquivo com o modelo treinado, usado pela API para gerar as previsões de vendas.
- requirements.txt: Lista de dependências do projeto.
- Procfile: Arquivo utilizado para definir os comandos que serão executados no deploy da aplicação (neste caso, usado pela Render para iniciar a aplicação Flask).
- Rossmann/: Pasta contendo a classe Rossmann, que é responsável por encapsular toda a lógica de processamento dos dados, incluindo limpeza, feature engineering e geração de previsões.
- Parameter/: Pasta onde estão armazenados parâmetros auxiliares e configuráveis que são utilizados na previsão de vendas, como informações de sazonalidade, feriados e detalhes de competições, entre outros.
- handler/: Contém o código que lida com as requisições da API, processa os dados de entrada, e integra com o modelo de machine learning para gerar as previsões.
