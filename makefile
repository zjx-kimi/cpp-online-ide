# Makefile for Python project

# 定义变量
PYTHON := python3
PIP := pip3
SRC_DIR := src
TEST_DIR := ./
VENV_DIR := venv
REQUIREMENTS_FILE := requirements.txt

# 默认目标
.DEFAULT_GOAL := help

# 帮助信息
help:
	@echo "Available targets:"
	@echo "  make install       - Install dependencies"
	@echo "  make test          - Run tests"
	@echo "  make clean         - Clean up"

# 安装依赖
install: $(VENV_DIR)
	$(PIP) install -r $(REQUIREMENTS_FILE)

# 创建虚拟环境
$(VENV_DIR):
	$(PYTHON) -m venv $(VENV_DIR)

# 运行测试
test:
	$(PYTHON) app.py

# 清理
clean:
	rm -rf $(VENV_DIR)

