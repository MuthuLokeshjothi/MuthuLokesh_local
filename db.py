from sqlalchemy import create_engine
import pandas as pd
import pymysql
engine = create_engine("mysql+pymysql://root:root@localhost:3306/im_deid")
df=pd.read_sql_query("SELECT id, patient_id, device_id, device_type, created_at, device_model, os_version, manufacturer, user_timezone, app_version, network_type, device_name, notifications_permission, device_uuid, modified_at FROM im_deid.mo_pha_pat_device_map;",engine)
print(df)