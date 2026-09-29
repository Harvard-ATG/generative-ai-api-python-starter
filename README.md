# AI API Harvard Demo

This script demonstrates how to configure and test Harvard's OpenAI API integrations to ensure your API keys are set up correctly.

## Harvard OpenAI API Services

### 1. OpenAI API for Community Developers

- **Documentation**: [AI Services - OpenAI API for Community Developers | Harvard ServiceNow KB Article](https://harvard.service-now.com/ithelp?id=kb_article&sys_id=197cc9d82b41ae94e401f84cfe91bf8c)
- **Base URL**: `https://go.apis.huit.harvard.edu/ais-openai-direct-limited-schools/v1`

### 2. OpenAI API for Course Use

- **Base URL**: `https://go.apis.huit.harvard.edu/ais-openai-direct/v2`
- **Access Request**: [Request OpenAI API key for classes, workshops, or other short-term contexts](https://harvard.az1.qualtrics.com/jfe/form/SV_8dZqSdJoKVE5EOi)

## Setup

This project uses [uv](https://docs.astral.sh/uv/getting-started/installation/) for dependency management, though it is optional.

To install dependencies without uv, use `pip install -r requirements.txt`.

## Configuration

In `.env`, set your OpenAI API key and choose your endpoint based on which Harvard API service you have access to.  Use the `.env.sample` as a guide.
