import dlt

@dlt.table              #标记下方函数为一张 DLT Live Table。
def factstream_stag():
    df = spark.readStream.table("spotify_cata.silver.factstream")      #直接读取 Databricks 内已存在的表
    return df           #把读取到的数据流返回，DLT 自动将其落地为 dimuser_stag 这张 DLT 表。


dlt.create_streaming_table(name="factstream") #提前定义一张空的流式 Delta 表 dimuser，作为 CDC/SCD 的最终目标表；

dlt.create_auto_cdc_flow(
    target="factstream",               #要写入的目标表名
    source = "factstream_stag",        #CDC 数据来源
    keys= ["stream_id"],              #主键 用来判断 “同一条记录”
    sequence_by= "stream_timestamp",       #排序字段：解决乱序、判断谁是最新
    stored_as_scd_type= 1,          # SCD1
    track_history_except_column_list= None,     #不追踪哪些列， None = 所有字段变化都生成新版本
    name= None,                     #给这个 CDC flow 起个名字， None = 默认用 target 名字（即 dimuser）
    once= False                     #False = 持续流式跑（实时 / 准实时同步）
)