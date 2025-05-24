## Python 优雅地处理文件路径 (pathlib)

\*\*来源:\*\*  Project X / utils / file\_handler.py

\*\*日期:\*\* 2025-04-20

\*\*代码片段:\*\*

\`\`\`python

from pathlib import Path

data\_dir = Path("./data/raw")

output\_file = data\_dir / "processed" / "output.csv"

# 检查目录是否存在，不存在则创建（包括父目录）

output\_file.parent.mkdir(parents=True, exist\_ok=True)

with open(output\_file, 'w') as f:

f.write("header\\n")
