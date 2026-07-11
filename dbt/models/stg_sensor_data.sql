-- Staging model for raw sensor data
with source as (
    select * from {{ source('raw', 'sensor_data') }}
),

renamed as (
    select
        sensor_id,
        event_timestamp,
        temperature,
        humidity,
        pressure,
        loaded_at
    from source
)

select * from renamed
