# SystemInfo API

一个基于 Flask 的系统硬件信息监控 API，支持获取 CPU、内存、GPU、磁盘等系统信息。

## 功能特点

- 实时获取系统硬件信息
- RESTful API 设计
- Docker 支持
- 跨平台兼容（Windows/Linux/MacOS）

## 系统信息包含

- CPU：型号、核心数、使用率
- 内存：总量、使用率、可用量
- GPU：型号、显存总量、使用量、温度（如果可用）
- 系统：操作系统类型、版本、主机名、架构
- 磁盘：总容量、已用空间、使用率

## 安装方式

### 方式一：直接运行

1. 克隆仓库
```bash
git clone git@github.com:nbazedong/SystemInfo.git
cd SystemInfo
```

2. 环境要求
- Python 3.7+
- pip 包管理工具

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 启动服务
```bash
python app.py
```
服务将在 http://localhost:5001 启动

### 方式二：Docker 部署

1. 构建镜像
```bash
docker build -t system-info .
```

2. 运行容器
```bash
docker run -d --privileged -p 5001:5001 --name system-info system-info
```

### 环境变量配置

可以通过设置以下环境变量来自定义服务配置：

- `PORT`: 服务端口号（默认：5001）
- `HOST`: 监听地址（默认：0.0.0.0）

示例：
```bash
PORT=8080 python app.py  # 使用8080端口启动服务
```
```
## API 接口

### 获取系统信息

- **接口**: `/api/system-info`
- **方法**: `GET`
- **返回格式**: JSON

返回示例：
```json
{
  "cpu": {
    "cpu_cores": 8,
    "cpu_model": "i386",
    "cpu_usage": 14.8
  },
  "disk": {
    "disk_usage": 61.8,
    "total_disk": 112.71,
    "used_disk": 10.61
  },
  "gpu": [],
  "memory": {
    "available_memory": 1.87,
    "memory_usage": 76.6,
    "total_memory": 8
  },
  "system": {
    "architecture": "x86_64",
    "hostname": "localhost",
    "os": "Darwin",
    "os_version": "Darwin Kernel Version 24.3.0"
  }
}
```
## 注意事项
1. Docker 部署时需要使用 --privileged 参数以获取硬件信息权限
2. GPU 信息仅在系统安装有 NVIDIA 显卡驱动时可用
3. 默认端口为 5001，可以通过环境变量或配置文件修改

## 许可证
MIT License

## 贡献
欢迎提交 Issue 和 Pull Request