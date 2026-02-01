# n8n-nodes-velatir

![Velatir](https://img.shields.io/badge/Velatir-Human--Approval--Gate-blue?style=flat-square)
![n8n-community-node-package](https://img.shields.io/badge/n8n-community--node-ff6d5a?style=flat-square)
![npm version](https://img.shields.io/npm/v/n8n-nodes-velatir?style=flat-square)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

**Human approval gate for n8n workflows with decision routing.** This community node integrates [Velatir](https://velatir.com) to pause your workflow until a human makes a decision, then routes the data to different outputs based on that decision.

## What does it do?

The Velatir node provides **smart decision routing**:

1. **Data flows in** → Gets sent to Velatir for human review
2. **Workflow pauses** → Waits for human decision
3. **Routes to different outputs** based on approval decision:
   - **Output 1**: Approved requests
   - **Output 2**: Declined requests
   - **Output 3**: Change requests with feedback

This gives you maximum flexibility to handle each decision type differently in your workflow.

## Installation

### Option 1: Community Nodes Panel (Recommended)
1. Go to **Settings > Community Nodes** in n8n
2. Select **Install**
3. Enter `n8n-nodes-velatir`
4. Select **Install**

### Option 2: Manual Installation
```bash
npm install n8n-nodes-velatir
```

## Setup

### 1. Get your Velatir API Key
- Sign up at [velatir.com](https://velatir.com)
- Get your API key from the dashboard

### 2. Add Credentials in n8n
- Go to **Settings > Credentials**
- Create new **Velatir API** credential
- Enter your API key
- Save

## Usage

### Basic Usage
Drag the **Velatir** node into your workflow and connect nodes to the outputs you need:

```
Trigger → [Your Data] → **Velatir** → [Approved: Process Data]
                                  → [Declined: Send Rejection Email]  
                                  → [Change Requested: Request More Info]
```

**The node will:**
- Automatically use your input data as the approval context
- Show the node name and description to approvers  
- Route data to different outputs based on the approval decision
- Include decision metadata in all outputs

### Simple Example
If you only care about approved requests, just connect the first output:

```
Trigger → [Your Data] → **Velatir** → [Process Approved Data]
```

### Configuration Options

| Field | Description | Default |
|-------|-------------|---------|
| **Function Name** | Name shown to approvers | Node name |
| **Description** | What this step does | Empty |
| **Polling Interval** | Check frequency (seconds) | 5 |
| **Timeout** | Max wait time (minutes) | 10 |
| **LLM Explanation** | AI context for approval decision | Empty |

## Examples

### Example 1: Content Review Workflow
```
Webhook → **Velatir** → [Approved: Publish Content]
                      → [Declined: Archive Content]
                      → [Changes Requested: Send to Editor]
```

### Example 2: User Registration with Feedback  
```
Form Submit → **Velatir** → [Approved: Create Account + Welcome Email]
                          → [Declined: Send Rejection Email]
                          → [Changes Requested: Request Additional Info]
```

### Example 3: Invoice Processing
```
New Invoice → **Velatir** → [Approved: Auto-Pay Invoice]
                          → [Declined: Mark as Disputed]  
                          → [Changes Requested: Request Clarification]
```

### Example 4: Simple Approval Gate
If you only need to process approved requests:
```
Manual Trigger → Set (Campaign Data) → **Velatir** → [Send Email]
```
Just connect the first output and leave the others unconnected.

## What Approvers See

When a request needs approval, your team will see:

- **Function Name**: "Send Email Campaign" (or whatever you set)
- **Description**: "Send marketing email to 1,500 customers" 
- **Arguments**: All the input data from your workflow
- **LLM Explanation**: AI context about why approval is needed (if provided)
- **Metadata**: Workflow context (ID, execution, behavior mode, etc.)

## Data Output

All outputs include the original data plus `_velatir` metadata:

```json
{
  "originalData": "your workflow data",
  "_velatir": {
    "reviewTaskId": "uuid-of-review-task",
    "state": "approved|declined|change_requested",
    "requestedChange": "feedback from approver (if any)"
  }
}
```

## Best Practices

### ✅ Do:
- Use descriptive node names (they become the function name)
- Add helpful descriptions for complex operations
- Place approval gates before critical/irreversible actions
- Set appropriate timeouts for your team's response time
- Provide LLM explanations for better approval context
- Connect the outputs you need (you don't have to use all three)
- Use the change requested output to implement feedback loops

### ❌ Don't:
- Put approval gates in loops (can create many approval requests)
- Set very short timeouts for non-urgent operations
- Forget that unconnected outputs will lose their data
- Ignore the `_velatir` metadata when processing decisions

## Error Handling

The node uses **decision routing** for all scenarios:

- **If approved**: Data flows to "Approved" output (Output 1)
- **If declined**: Data flows to "Declined" output (Output 2)  
- **If changes requested**: Data flows to "Change Requested" output (Output 3) with feedback
- **If timeout**: Workflow stops after the configured timeout
- **If API error**: With "Continue on Fail" enabled, errors flow to "Declined" output
- **If API error**: With "Continue on Fail" disabled, workflow stops with error message

## Workflow Patterns

### Pattern 1: Simple Approval
```
Data → **Velatir** → [Approved: Process Data]
```
Only connect the approved output for basic approval gates.

### Pattern 2: Full Decision Handling
```
Data → **Velatir** → [Approved: Process Data]
                   → [Declined: Log Rejection]
                   → [Changes: Request Info]
```
Handle all three decision types differently.

### Pattern 3: Feedback Loop
```
Data → **Velatir** → [Approved: Process]
                   → [Declined: Archive]
                   → [Changes: Edit] → **Velatir** (New Review)
```
Use change requests to improve and resubmit.

### Pattern 4: Escalation Workflow
```
Data → **Velatir** → [Approved: Execute]
                   → [Declined: End]
                   → [Changes: Escalate] → Senior **Velatir** → Execute
```
Escalate change requests to higher approval levels.

### Pattern 5: Conditional Approval
```
Data → IF (high_value?) → **Velatir** → [Process]
                        → Direct Process
```
Only require approval for certain conditions.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Request timeout" | Increase timeout or check if approvers are available |
| "API key invalid" | Verify credential configuration in n8n |
| "Request declined" | Data flows to declined output - check approver feedback |
| Node doesn't appear | Restart n8n after installation |
| "Unexpected state" | Update to latest node version (API may have changed) |
| Data not flowing to expected output | Check the `_velatir.state` field in your data |
| Missing data on outputs | Connect only the outputs you need, unconnected outputs lose data |

## Minimal Examples

### Simple Approval
1. **Manual Trigger** 
2. **Set** node with: `{"message": "Hello World"}`
3. **Velatir** node (default settings)
4. **No Op** node connected to "Approved" output

When you run this:
- Your approver sees: Function "Velatir" needs approval with args `{"message": "Hello World"}`
- If approved: Data flows to No Op with `_velatir` metadata
- If declined/changed: Data flows to unconnected outputs (lost)

### Full Decision Routing
1. **Manual Trigger**
2. **Set** node with: `{"message": "Hello World"}`
3. **Velatir** node 
4. **No Op** node connected to "Approved" output
5. **Set** node connected to "Declined" output with message "Request declined"
6. **Set** node connected to "Change Requested" output with message "Changes needed"

When you run this, the workflow routes to different paths based on the approval decision, and you can handle each case appropriately.

## Support

- 📖 [Velatir Documentation](https://www.velatir.com/docs)
- 💬 [n8n Community Forum](https://community.n8n.io)
- 🐛 [Report Issues](https://github.com/velatir/n8n-nodes-velatir/issues)
- 📧 [Contact Support](mailto:hello@velatir.com)

## License

[MIT](LICENSE)