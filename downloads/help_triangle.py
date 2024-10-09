# 設定金字塔的高度
height = 30

# 使用 for 迴圈列印金字塔
for i in range(height):
    # 列印空格
    print('　' * (height - i - 1 + 2), end='')  # 增加 2 個空格
    # 列印星號
    print('＊' * (2 * i + 1))
