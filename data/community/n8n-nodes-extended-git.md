![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-extended-git

This repo helps you get started building your own custom integrations for [n8n](https://n8n.io). It includes the node linter and other dependencies.
This repository also provides a **Git Extended** node that lets you run Git commands directly from your workflows.

To make your custom node available to the community, you must create it as an npm package, and [submit it to the npm registry](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry).

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and pnpm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Using this starter

These are the basic steps for working with the starter. For detailed guidance on creating and publishing nodes, refer to the [documentation](https://docs.n8n.io/integrations/creating-nodes/).

1. [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate) from this template repository.
2. Clone your new repo:
   ```
   git clone https://github.com/<your organization>/<your-repo-name>.git
   ```
3. Run `npm i` to install dependencies.
4. Open the project in your editor.
5. Add your node and credential files to `/nodes` and `/credentials`.
6. Update the `package.json` to match your details.
7. Run `npm lint` to check for errors or `npm lintfix` to automatically fix errors when possible.
8. Test your node locally. Refer to [Run your node locally](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/) for guidance.
9. Replace this README with documentation for your node. Use the [README_TEMPLATE](README_TEMPLATE.md) to get started.
10. Update the LICENSE file to use your details.
11. [Publish](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry) your package to npm.

## Git Extended node

This repository includes a Git Extended node located in `/nodes/GitExtended`. It lets you execute common Git commands inside your workflows. The node supports operations like `clone`, `init`, `add`, `commit`, `push`, `lfsPush`, `pull`, `status`, `log`, `switch`, `checkout`, `merge`, `applyPatch`, `branches`, `createBranch`, `deleteBranch`, `renameBranch`, `commits`, `fetch`, `rebase`, `cherryPick`, `revert`, `reset`, `stash`, `tag`, and `configUser`.
The push operation includes a **Force Push** option that appends `--force` to the command when enabled.
Enable **Push LFS Objects** to run `git lfs push --all` automatically before pushing.
Enable **Skip LFS Push** to set `GIT_LFS_SKIP_PUSH=1` and skip uploading LFS objects during the push.
Enable **Skip LFS Smudge** to set `GIT_LFS_SKIP_SMUDGE=1` when cloning, pulling, or fetching so Git LFS objects are not downloaded.
Use `lfsPush` to manually upload Git LFS objects when the remote requires them.
Enable **Skip Stdout** to discard command output and avoid `stdout maxBuffer length exceeded` errors when commands produce large output.

The *Remote* parameter accepts either a remote name (such as `origin`) or a full repository URL. This lets you push or pull from a configured remote or directly specify another repository.

Example usage:

```text
Remote: origin
Branch: main
```

```text
Remote: https://github.com/example/repo.git
Branch: main
```

Every operation requires a **Repository Path** parameter that defines the directory from which the Git command is executed. For `clone`, the repository will be created inside this directory.

The `applyPatch` operation uses `git apply` to apply a patch file. You can provide the patch text directly or specify a path to a patch file. Enable the *Binary* option when applying binary patches.

### Running Git commands

The node relies on the `git` binary available on the machine running n8n. Make sure `git` is installed and accessible from the command line.


## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
