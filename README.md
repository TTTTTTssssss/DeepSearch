python --version  # 应该显示 Python 3.10.x 或更高
node --version    # 应该显示 v16.x.x 或更高
npm --version     # 应该显示 8.x.x 或更高

1) 启动后端
# 进入目录
cd deepsearch/backend

# 安装依赖
pip install -e .

# 配置环境变量，编辑.env文件，填入API密钥
cp .env.example .env

# 启动后端
python src/main.py


2) 启动前端
# 进入目录
cd deepsearch/frontend

# 安装依赖
npm install

# 启动前端
npm run dev


