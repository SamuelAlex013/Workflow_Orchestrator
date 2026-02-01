8th Wall MCP Server

This repository scaffolds a Model Context Protocol (MCP) server to work with 8th Wall. It supports three modes:

- Docs mode: fetch and expose 8th Wall Studio docs as resources and tools (search/read).
- API mode: wrap 8th Wall endpoints to manage apps and scenes (requires credentials).
- Local mode: mirror BlenderMCP-style capabilities for a local web XR project (project/file ops, asset search/download stubs, strategy guidance).

By default, the server starts with a minimal tool and placeholders you can extend after confirming your preferred mode.

Quick start

- Requirements: Node.js 18+ (for native `fetch`), npm
- Install deps: `npm install`
- Build: `npm run build`
- Run (stdio): `node dist/index.js`

MCP client configuration

Example for Claude Desktop `mcpServers` in `config.json`:

```
{
  "mcpServers": {
    "8thwall": {
      "command": "node",
      "args": ["dist/index.js"],
      "env": {
        "MODE": "local",          // default; use "docs" or "api" if needed
        "EIGHTHWALL_BASE_URL": "https://www.8thwall.com",
        "EIGHTHWALL_DOCS_ROOT": "https://www.8thwall.com/docs/",
        "EIGHTHWALL_API_KEY": "<optional-if-API-mode>",
        "PROJECT_ROOT": "./project"
      }
    }
  }
}
```

Claude Desktop quick config (Local mode)

Paste into Claude Desktop > Settings > Developer > Edit Config:

```
{
  "mcpServers": {
    "8thwall": {
      "command": "node",
      "args": ["dist/index.js"],
      "env": {
        "MODE": "local",
        "PROJECT_ROOT": "./project"
      }
    }
  }
}
```

Cursor quick config

- Global server: Settings → MCP → Add New Global MCP Server, then paste:

```
{
  "mcpServers": {
    "8thwall": {
      "command": "node",
      "args": ["dist/index.js"],
      "env": {
        "MODE": "local",
        "PROJECT_ROOT": "./project"
      }
    }
  }
}
```

- Project server: create `.cursor/mcp.json` in your project root with the same JSON.

VS Code (MCP extension) quick steps

- Install an MCP-compatible extension (e.g., “Model Context Protocol” or equivalent).
- Add a new stdio server with:
  - Name: `8thwall`
  - Command: `node`
  - Args: `dist/index.js`
  - Env: `MODE=local`, `PROJECT_ROOT=./project`

End-to-end quick test

- Ask Claude: "Scaffold an A‑Frame scene and start the dev server."
  - Expected tools: `project.scaffold`, then `devserver.start` → opens `http://127.0.0.1:5173/`.
- Ask: "Add a red box at (0, 1, -2) sized 1x1x1 and a directional light at (2, 3, 2)."
  - Tools: `scene.add_primitive`, `scene.add_light`.
- Ask: "Set an HDRI environment from this URL and also use it as background: https://dl.polyhaven.org/file/ph-assets/HDRIs/hdr/1k/studio_small_08_1k.hdr"
  - Tool: `scene.set_environment_hdr`.
- Ask: "Download the DamagedHelmet GLB from Khronos samples and add it at y=1.2 with scale 0.5."
  - Tools: `assets.download_url` with
    - URL: `https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb`
    - filename: `models/DamagedHelmet.glb` (relative to `project/assets/`)
  - Then: `scene.add_gltf_model` with `src: assets/models/DamagedHelmet.glb`, `position: [0,1.2,-2]`, `scale: [0.5,0.5,0.5]`.
- Optional: "Export the project as a zip for Studio upload."
  - Tool: `project.export_zip` → returns archive path.

If the preview doesn’t open on `localhost`, use `http://127.0.0.1:5173/`.

8th Wall Desktop App integration

- The Desktop App stores projects under `~/Documents/8th Wall/<YourProject>` by default.
- You can point the MCP server to a Desktop project so all edits reflect in the app:
  - Option A (config): set `PROJECT_ROOT` to the project path in your MCP client env.
  - Option B (tools): use `desktop_list_projects` to discover paths, then `desktop_set_project` with a folder name, or `project_set_root` with the full path. Confirm with `project_get_root`.
- After setting the root, use the same scene and asset tools (`scene_*`, `assets_*`, `project_*`). The Desktop app typically detects file changes; if not, hit its refresh/build button.

Environment variables

- `MODE`: `local`, `docs`, or `api`. Defaults to `local`.
- `EIGHTHWALL_DOCS_ROOT`: Base URL for docs. Defaults to `https://www.8thwall.com/docs/`.
- `EIGHTHWALL_BASE_URL`: Origin for runtime links. Defaults to `https://www.8thwall.com`.
- `EIGHTHWALL_API_BASE`: Base API URL for 8th Wall (only in API mode). Placeholder, set to the correct API host.
- `EIGHTHWALL_API_KEY`: API token/key (only in API mode).
- `MOCK_8THWALL`: If set to `1`, the server returns mocked data for API tools.
// Local mode
- `PROJECT_ROOT`: Filesystem path for the local project (default `./project`).

Tools and resources

- `health_ping`: Simple health check tool.
 - `docs_get_page`: Fetch a docs page and return sanitized text.
 - `docs_search`: Basic keyword search across a set of doc URLs (naive fetch-and-scan).
- `app.list`: List apps (API mode; mocked unless API wired up).
- `app.get`: Get a single app by ID (API mode; mocked unless API wired up).

Local mode (includes docs tools)

- `project_get_info`, `project_list_files`, `project_read_file`, `project_write_file`, `project_delete_file`, `project_move_file`
- `project_scaffold`: create a minimal web XR shell (index.html, main.js, styles.css)
  - Args: `template` = `aframe` (default) or `three`, `overwrite` (bool)
- `assets_status`: report availability of PolyHaven integration
- `assets_search_polyhaven`: search PolyHaven (public API; requires network)
- `assets_download_url`: download any file into `project/assets/`
- `prompts_asset_strategy`: guidance on sourcing/organizing assets
- `devserver_start` / `devserver_stop`: serve `PROJECT_ROOT` locally for quick preview
 - `scene_detect_engine`: detect if the project uses A‑Frame or Three.js
 - `scene_add_gltf_model`: inject a GLTF/GLB model into the scene (A‑Frame entity or Three.js GLTFLoader)
 - `scene_set_background_color`: set scene background color (A‑Frame background or Three.js scene.background)
 - `scene_add_primitive`: add primitives (box/sphere/cylinder/plane), with color/size/pos/rot/scale
 - `scene_add_light`: add ambient/hemisphere/directional/point light
 - `scene_set_environment_hdr`: set environment from HDR/EXR (sky in A‑Frame; environment/background in Three.js)
 - `scene_add_animation`: add a simple spin animation (A‑Frame entity or Three.js loop)
 - `scene_add_textured_plane`: add a plane with an image texture
 - `scene_add_orbit_controls` (Three.js): add OrbitControls
 - `scene_add_grid_helper` (Three.js): add a grid helper
 - `scene_add_floor` (Three.js): add a simple floor plane

PolyHaven helpers

- `assets_polyhaven_categories`: list categories for a given type
- `assets_polyhaven_files`: get file metadata for an asset id

Other helpers

- `assets_unzip`: unzip an archive into `project/assets/...`

Note on 8th Wall API endpoints

This scaffold does not embed non-public information. If you intend to use API mode, set `EIGHTHWALL_API_BASE` and provide a valid `EIGHTHWALL_API_KEY`. Then implement the specific endpoints in `src/clients/8thwallClient.ts` according to your access and docs.

Development

- Type-check: `npm run typecheck`
- Dev run with ts-node: `npm run dev`

HTTP bridge for n8n

If you want to call the server’s tools from n8n (via HTTP Request nodes), run the included HTTP bridge:

- Build: `npm run build`
- Start bridge: `HTTP_PORT=8787 MODE=local PROJECT_ROOT=./project npm run http`
  - Defaults: host `127.0.0.1`, port `8787`. Configure with `HTTP_HOST` and `HTTP_PORT`.
  - Lists tools: `GET http://127.0.0.1:8787/tools`
  - Invoke a tool: `POST http://127.0.0.1:8787/tool/<toolName>` with JSON body (args).

Example n8n HTTP requests

- Download a model into `project/assets/models/`:
  - Method: POST
  - URL: `http://127.0.0.1:8787/tool/assets_download_url`
  - JSON Body:
    `{ "url": "https://example.com/model.glb", "filename": "models/MyModel.glb" }`

- Add the model to the scene (A‑Frame or Three.js auto-detected from `index.html`):
  - Method: POST
  - URL: `http://127.0.0.1:8787/tool/scene_add_gltf_model`
  - JSON Body:
    `{ "src": "assets/models/MyModel.glb", "position": [0,1.2,-2], "scale": [0.5,0.5,0.5] }`

- Start the local dev server for preview:
  - Method: POST
  - URL: `http://127.0.0.1:8787/tool/devserver_start`
  - JSON Body:
    `{ "port": 5173 }`
  - Response includes: `{ url: "http://127.0.0.1:5173/", running: true }`.

**n8n Nodes**

- A publishable n8n community package is included at `n8n-nodes-8thwall/`.
- It adds:
  - A flexible node “8th Wall MCP Tool” which calls the HTTP bridge tools.
  - A Router node that turns free‑text requests into tool + args items you can feed into the MCP node via expressions.
- Quick use:
  - Build and run the HTTP bridge here (see above).
  - Build the package: `cd n8n-nodes-8thwall && npm install && npm run build`.
  - In n8n, enable Community Nodes and install from this folder (or from npm if published as `n8n-nodes-8thwall`).
  - Create credentials “8th Wall MCP Bridge API” with Base URL `http://127.0.0.1:8787`.
  - Add the MCP node and choose a tool; or use the Router → MCP pattern by setting Tool Name (Custom) = `{{$json.tool}}` and Args (JSON) = `{{$json.args}}`.

Notes

- The HTTP bridge reuses the same tool implementations as the MCP server; no duplication.
- Use `PROJECT_ROOT` to point at your 8th Wall Desktop project for in‑place edits.
- CORS is open (`*`) for convenience on localhost; lock down `HTTP_HOST`/reverse‑proxy in production contexts.

Project structure

- `src/index.ts`: Server entry. Registers tools/resources for docs or API modes.
- `src/tools/docs.ts`: Docs-mode tools (fetch/read/search pages).
- `src/tools/app.ts`: API-mode tools (list/get apps, mocked by default).
- `src/clients/8thwallClient.ts`: Minimal HTTP client wrapper for API mode.
- `src/types.ts`: Shared types for App/Scene.
 - `src/tools/assets.ts`: Asset search/download + unzip
 - `src/tools/project.ts`: Project tools (file ops, scaffold, export)
 - `src/tools/scene.ts`: Scene-building helpers (primitives, lights, models, env, etc.)

Security

Never commit real API keys. Use environment variables or your MCP client’s secret storage.

Contributing & License

- Contributions welcome! See `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.
- Security reports: see `SECURITY.md`.
- License: MIT (see `LICENSE`).
