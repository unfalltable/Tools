import os
import shutil

# 克隆仓库
# git clone https://github.com/trustwallet/assets

# TrustWallet 仓库路径（改成你本地的实际路径）
SRC_DIR = r"D:\other\assets\blockchains\smartchain\assets"
# 输出目录
DST_DIR = r"D:\other\bnb_logos"

os.makedirs(DST_DIR, exist_ok=True)

count = 0

for root, dirs, files in os.walk(SRC_DIR):
    if "logo.png" in files:
        # 获取合约地址（目录名）
        address = os.path.basename(root).lower()
        src_file = os.path.join(root, "logo.png")
        dst_file = os.path.join(DST_DIR, f"{address}.png")

        try:
            shutil.copy2(src_file, dst_file)
            count += 1
            print(f"✅ 已复制: {address}")
        except Exception as e:
            print(f"⚠️ 出错: {address}, {e}")

print(f"\n完成！共复制 {count} 个 logo 到 {DST_DIR}")
