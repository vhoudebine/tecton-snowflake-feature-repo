#from tecton import PushSource, SnowflakeConfig, Entity, Aggregation, StreamFeatureView
#from tecton.aggregation_functions import last
#from tecton.types import Field, String, Timestamp, Int64
#from datetime import datetime, timedelta
#from tecton import stream_feature_view, BatchTriggerType
#
#device = Entity(name='device', join_keys=['VISITORID'])
#
#input_schema = [
    #Field(name='CREATED_AT', dtype=Timestamp),
    #Field(name='VISITORID', dtype=String),
    #Field(name='ID', dtype=Int64)
#]
#
#orders_push = PushSource(
                        #name='auth_request_source',
                        #schema=input_schema,
                        #description='Push source for billie orders',
                        #batch_config=SnowflakeConfig(
                            #query="""
                            #SELECT VISITORID, ID, CREATED_AT FROM BILLIE_SAMPLE_DATA.PUBLIC.AUTH_REQUESTS_FULL
                            #""",
                            #timestamp_field="CREATED_AT"
                        #),
                        #tags={'release': 'staging'}
                        #)
#
#re_count_push_fv = StreamFeatureView(
    #name="n_order_last_5min_per_deviceid",
    #source=FilteredSource(orders_push),
    #entities=[device],
    #online=True,  
    #offline=True,
    #feature_start_time=datetime(2023, 5, 20),
    #batch_schedule=timedelta(days=1),
    #aggregations=[
        #Aggregation(column="ID", function="count", time_window=timedelta(minutes=5), name="nb_orders_per_deviceid_last_5"),
    #],
    #tags={"release": "production"},
    #owner="vince@tecton.ai",
    #description="The count of orders per email in last 5 min",
#)