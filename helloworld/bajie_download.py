import os
#模型下载
from modelscope.hub.snapshot_download import snapshot_download


# save_dir是模型保存到本地的目录
save_dir="../models"

snapshot_download('JimmyMa99/BaJie-Chat-mini', 
                  cache_dir=save_dir)
                  
