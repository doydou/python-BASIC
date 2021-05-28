#添加一个play按钮
def __init__(self, ai_settings):
    """初始化统计信息"""
    self.ai_settings = ai_settings
    self.reset_stats()

    #让游戏一开始处于非活动状态
    self.game_active = False

