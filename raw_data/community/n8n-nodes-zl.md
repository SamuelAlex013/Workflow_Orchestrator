# n8n-nodes-zl
Fix Err credentials QR Login

# Setup

1.  Mở trình soạn thảo n8n của bạn.
2.  Vào Settings > Community Nodes.
3.  Tìm kiếm "n8n-nodes-zl".
4.  Nhấp vào Install.
5.  Tải lại trình soạn thảo.

# dev

# In your node directory
pnpm run build
pnpm link

# In ~/.n8n directory run
mkdir custom 
cd custom 
pnpm init

pnpm link n8n-nodes-zl
