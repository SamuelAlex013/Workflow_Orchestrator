# n8n-nodes-patreon

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

[n8n](https://www.n8n.io)

## What is the Patreon?

Patreon is a membership-based platform that provides a way for creators to receive financial support from their fans or patrons on a recurring basis. Creators can create content such as videos, podcasts, comics, music, and more, and offer exclusive rewards and perks to their patrons who support them financially through Patreon.

The platform allows creators to set up multiple tiers of rewards for their patrons based on their level of support, and it also provides tools for communication, community building, and content distribution.

Patreon takes a small percentage of the funds as a service fee, and the rest is deposited directly into the creator's account. This allows creators to monetize their creative work and build sustainable careers while offering their fans an opportunity to support them directly.


## How to install

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-patreon` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

### Manual installation

To get started install the package in your n8n root directory:

`npm install n8n-nodes-patreon`

For Docker-based deployments, add the following line before the font installation command in your [n8n Dockerfile](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/Dockerfile):

`RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-patreon`

## How to use

### Credentials setup

You need to register a Ouath2 client on [Patreon](https://www.patreon.com/portal/registration/register-clients).

- ![1st step](https://raw.githubusercontent.com/pigri/n8n-nodes-patreon/master/assets/1st_step.png)
- ![2nd step](https://raw.githubusercontent.com/pigri/n8n-nodes-patreon/master/assets/2nd_step.png)
- ![3rd step](https://raw.githubusercontent.com/pigri/n8n-nodes-patreon/master/assets/3rd_step.png)

You need to copy your Client ID and Client Secret to N8N.

- ![4th step](https://raw.githubusercontent.com/pigri/n8n-nodes-patreon/master/assets/4th_step.png)
