# Notion C2 Profile

## Overview

The Notion C2 profile uses the [Notion API](https://developers.notion.com/) as a covert
communication channel between Mythic agents and the C2 server.

Each agent message is stored as a page in a shared Notion database. The server polls that
database, forwards messages to Mythic, and writes responses back for the agent to pick up.

Traffic is indistinguishable from legitimate Notion usage — HTTPS requests to `api.notion.com`.

## Database schema

Create a Notion database with the following properties:

| Property   | Type     | Description                          |
|------------|----------|--------------------------------------|
| `uuid`     | Title    | Unique message identifier            |
| `direction`| Select   | `in` (agent→server) / `out` (server→agent) |
| `agent_id` | Text     | UUID of the originating agent        |
| `processed`| Checkbox | Set to true once consumed            |

The `created_time` property is automatically added by Notion.

## Parameters

| Parameter            | Required | Default | Description                               |
|----------------------|----------|---------|-------------------------------------------|
| `integration_token`  | Yes      | —       | Notion integration token (`ntn_...`)   |
| `database_id`        | Yes      | —       | ID of the shared Notion database          |
| `callback_interval`  | No       | 10      | Polling interval in seconds               |
| `callback_jitter`    | No       | 10      | Jitter percentage (0–50)                  |

## Setup

1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations) and create an integration.
2. Copy the **Integration Token**.
3. Create a database with the schema above.
4. Share the database with your integration (**Share** → invite).
5. Copy the **Database ID** from the page URL.
