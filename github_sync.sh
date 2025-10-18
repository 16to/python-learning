#!/bin/bash

# Python学习教程 - GitHub快速同步脚本
# 使用方法: bash github_sync.sh

echo "=========================================="
echo "   Python学习教程 - GitHub同步工具"
echo "=========================================="
echo ""

# 检查是否已初始化Git
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
    echo "✓ Git仓库初始化完成"
    echo ""
fi

# 配置Git用户信息（如果未配置）
if [ -z "$(git config user.name)" ]; then
    echo "⚙️  配置Git用户信息"
    echo "请输入你的GitHub用户名："
    read username
    git config user.name "$username"
    
    echo "请输入你的GitHub邮箱："
    read email
    git config user.email "$email"
    echo "✓ Git用户信息配置完成"
    echo ""
fi

# 查看当前状态
echo "📊 当前文件状态："
git status --short
echo ""

# 添加所有文件
echo "➕ 添加文件到Git..."
git add .
echo "✓ 文件添加完成"
echo ""

# 提交更改
echo "请输入提交信息（或按Enter使用默认信息）："
read commit_msg

if [ -z "$commit_msg" ]; then
    commit_msg="更新Python学习教程 - $(date '+%Y-%m-%d %H:%M:%S')"
fi

git commit -m "$commit_msg"
echo "✓ 提交完成"
echo ""

# 检查是否已关联远程仓库
if git remote | grep -q 'origin'; then
    echo "🚀 推送到GitHub..."
    git push origin main 2>/dev/null || git push origin master
    echo "✓ 推送完成！"
else
    echo "⚠️  尚未关联GitHub仓库"
    echo ""
    echo "请按照以下步骤操作："
    echo "1. 访问 https://github.com/new"
    echo "2. 创建一个新仓库（建议名称：python-learning）"
    echo "3. 复制仓库URL（如：https://github.com/username/python-learning.git）"
    echo ""
    echo "请输入GitHub仓库URL："
    read repo_url
    
    if [ ! -z "$repo_url" ]; then
        git remote add origin "$repo_url"
        git branch -M main
        git push -u origin main
        echo "✓ 推送完成！"
    else
        echo "❌ 未输入仓库URL，推送已取消"
        echo ""
        echo "手动关联仓库的命令："
        echo "  git remote add origin <你的仓库URL>"
        echo "  git branch -M main"
        echo "  git push -u origin main"
    fi
fi

echo ""
echo "=========================================="
echo "           🎉 同步完成！"
echo "=========================================="
echo ""
echo "📝 其他电脑克隆仓库："
echo "  git clone <你的仓库URL>"
echo ""
echo "🔄 日常同步："
echo "  bash github_sync.sh  # 推送更新"
echo "  git pull             # 拉取更新"
echo ""
