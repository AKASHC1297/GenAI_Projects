---
table_name: fact_app_sessions
domain: product_analytics
table_type: fact
grain: one_record_per_app_session

table_description: >
  Fact table capturing application usage sessions for both riders and drivers.
  The grain of the table is one record per user session.

fields:
  - field_name: session_id
    data_type: STRING
    key_type: PRIMARY_KEY
    description: Unique identifier for each application session.

  - field_name: user_id
    data_type: STRING
    key_type: NONE
    description: Identifier for the user initiating the session (can be rider or driver).

  - field_name: user_type
    data_type: STRING
    key_type: NONE
    description: Indicates whether the session belongs to a rider or driver.

  - field_name: platform
    data_type: STRING
    key_type: NONE
    description: Platform used during session (iOS, Android, Web).

  - field_name: session_start_time
    data_type: TIMESTAMP
    key_type: NONE
    description: Timestamp when the session started.

  - field_name: session_end_time
    data_type: TIMESTAMP
    key_type: NONE
    description: Timestamp when the session ended.

  - field_name: session_duration_seconds
    data_type: INTEGER
    key_type: NONE
    description: Total duration of the session in seconds.
---

# Table: fact_app_sessions

## Description
This fact table captures **user activity sessions within the mobile application**.

**Grain:** One record per app session.

It supports **product analytics and engagement analysis**.

---

## Field Definitions

| Field Name | Data Type | Key Type | Description |
|------------|-----------|----------|-------------|
| session_id | STRING | Primary Key | Unique identifier for each session |
| user_id | STRING | None | Identifier for rider or driver |
| user_type | STRING | None | Indicates rider or driver |
| platform | STRING | None | Device platform used |
| session_start_time | TIMESTAMP | None | Time when session started |
| session_end_time | TIMESTAMP | None | Time when session ended |
| session_duration_seconds | INTEGER | None | Total duration of session |

---

## Analytical Use Cases

- App engagement analysis
- Session length analysis
- Platform usage trends
