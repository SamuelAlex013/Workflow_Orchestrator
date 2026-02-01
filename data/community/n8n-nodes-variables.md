# n8n-nodes-variables

![n8n Variables Nodes](https://img.shields.io/badge/n8n-community%20node-blueviolet)
![npm version](https://img.shields.io/npm/v/n8n-nodes-variables)
![npm downloads](https://img.shields.io/npm/dm/n8n-nodes-variables)

**Typed global variables for n8n workflows** - Manage variables like real programming languages with strong typing support!

## 🎯 **Solve Real Problems**

### **❌ The Problem n8n Users Face:**
```
HTTP Request (uses URL) → Process Data → IF (has more pages?)
     ↑                                           ↓
     └── Can't access new URL from here ←─── Set new URL
```

**Common Issues:**
- ❌ Variables only accessible from previously executed nodes
- ❌ Can't modify upstream node parameters from downstream nodes
- ❌ No clean way to manage pagination/loops
- ❌ Workflow state management is complex

### **✅ Our Solution:**
```
1. Variables Node: Initialize URL = "https://example.com/page/1"
2. HTTP Request: Uses {{ $workflow.variables.URL }}
3. Process Data
4. IF (has more pages?) 
   └─ True: Variables Node: Set URL = "https://example.com/page/2"
5. Loop back - HTTP Request automatically uses new URL!
```

## 📦 **Three Powerful Nodes Included**

### **1. Variables (Main Node)** 
🎯 **Perfect for: Loops, pagination, state management**
- **Typed variables**: String, Number, Boolean, JSON, Date
- **Global access**: Use anywhere with `$workflow.variables.VARIABLE_NAME`
- **Clean output**: Returns just the variables as key-value pairs
- **Type-specific inputs**: Different UI fields based on variable type

### **2. Variables Dashboard**
📊 **Perfect for: Debugging, bulk operations**
- **Table view**: See all variables at once
- **Bulk operations**: Set multiple variables simultaneously  
- **No connections needed**: Works as sticky note
- **Sort & filter**: Organize variables by type/name

### **3. Global Variables**
🌐 **Perfect for: Cross-workflow sharing**
- **Instance-wide**: Share variables across all workflows
- **Persistent**: Variables survive workflow restarts
- **Legacy support**: For existing implementations

## 🚀 **Quick Start**

### **Installation**

```bash
# Community Nodes (Recommended)
1. Go to Settings → Community Nodes in n8n
2. Install: n8n-nodes-variables

# Manual Installation  
npm install n8n-nodes-variables
```

### **Basic Usage Example**

```javascript
// 1. Initialize Variables
Variables Node → Initialize Variables:
- URL (String): "https://api.example.com/page/1"
- pageNumber (Number): 1

// 2. Use in HTTP Request
HTTP Request → URL: {{ $workflow.variables.URL }}

// 3. Update for next iteration
Variables Node → Set Variable:
- Name: URL  
- Type: String
- Value: {{ $json.nextPageUrl }}

// 4. Loop back automatically!
```

## 💡 **Real-World Use Cases**

### **🔄 Pagination Scraping**
```javascript
// Perfect for scraping multiple pages
Initialize: URL = "https://site.com/page/1", pageNum = 1
HTTP Request: {{ $workflow.variables.URL }}
Process Data
IF hasMorePages:
  ├─ Set URL = nextPageURL  
  ├─ Set pageNum = pageNum + 1
  └─ Loop back to HTTP Request
```

### **🔁 API Rate Limiting**
```javascript
// Retry logic with counters
Initialize: retryCount = 0, maxRetries = 3
HTTP Request: Call API
IF request failed && retryCount < maxRetries:
  ├─ Set retryCount = retryCount + 1
  ├─ Wait node: 5 seconds
  └─ Loop back to HTTP Request
```

### **📊 Batch Processing**
```javascript
// Process items with progress tracking
Initialize: processed = 0, total = 100, results = []
Process Item
Set processed = processed + 1
Set results = [...results, newResult]
IF processed < total: Loop back
```

## 🎨 **Variable Types**

| Type | Input Field | Example | Use Case |
|------|-------------|---------|----------|
| **String** | Text field | `"https://api.com"` | URLs, API keys, messages |
| **Number** | Number input | `42` | Counters, limits, IDs |  
| **Boolean** | Toggle switch | `true` | Feature flags, conditions |
| **JSON** | JSON editor | `{"key": "value"}` | Complex objects, configs |
| **Date** | Date picker | `2024-01-01T00:00:00Z` | Timestamps, schedules |

## 🔧 **All Operations**

### **Variables Node**
- **Initialize Variables**: Set up multiple typed variables
- **Set Variable**: Update single variable with type validation
- **Get Variable**: Retrieve specific variable value
- **View All Variables**: Get all variables as clean object
- **Clear All Variables**: Reset all variables

### **Variables Dashboard**  
- **View All**: Table display of all variables
- **Bulk Set**: Update multiple variables at once
- **Clear All**: Reset with confirmation

### **Global Variables**
- **Set Variable**: Store instance-wide variable
- **Get Variable**: Retrieve instance-wide variable  
- **List All**: Show all global variables

## 📖 **Expression Access**

```javascript
// Use variables anywhere in n8n
{{ $workflow.variables.URL }}           // String variable
{{ $workflow.variables.pageNumber }}    // Number variable  
{{ $workflow.variables.isEnabled }}     // Boolean variable
{{ $workflow.variables.config.timeout }} // JSON object property

// In Function nodes
const url = $workflow.variables.URL;
const page = $workflow.variables.pageNumber;
const settings = $workflow.variables.config;

// In IF conditions  
{{ $workflow.variables.retryCount < $workflow.variables.maxRetries }}

// In HTTP Request headers
{
  "Authorization": "Bearer {{ $workflow.variables.apiToken }}",
  "Page": "{{ $workflow.variables.pageNumber }}"
}
```

## 🔄 **Migration Guide**

### **From Manual Variable Management**
```javascript
// Before: Complex manual tracking
Function Node: return { url: "page/1", count: 0 };

// After: Clean typed variables  
Variables Node: Initialize URL (String) = "page/1", count (Number) = 0
```

### **From Static Values**
```javascript
// Before: Hardcoded values
HTTP Request: URL = "https://api.com/page/1"

// After: Dynamic variables
HTTP Request: URL = {{ $workflow.variables.baseURL }}/page/{{ $workflow.variables.pageNumber }}
```

## 🎯 **Best Practices**

### **✅ Do's**
- Use **Variables node** for workflow-specific state
- Use **Variables Dashboard** for debugging/development  
- Use **Global Variables** for cross-workflow sharing
- Initialize variables at workflow start
- Use descriptive variable names

### **❌ Don'ts**  
- Don't mix variable management approaches
- Don't store sensitive data in Global Variables
- Don't use variables for one-time values
- Don't forget to clear variables when testing

## 🐛 **Troubleshooting**

### **Variables Not Updating**
```javascript
// ❌ Wrong: Using old syntax
{{ $json.variables.URL }}

// ✅ Correct: Use workflow variables
{{ $workflow.variables.URL }}
```

### **Type Errors**
```javascript
// ❌ Wrong: String in number field
pageNumber (Number) = "5"  

// ✅ Correct: Proper type
pageNumber (Number) = 5
```

### **Scope Issues**
```javascript
// Workflow Variables: Only within same workflow
// Global Variables: Across all workflows  
// Choose the right scope for your use case
```

## 📈 **Performance Tips**

- **Initialize once**: Set up all variables at workflow start
- **Batch updates**: Use bulk operations when possible
- **Clean up**: Clear variables when workflow completes
- **Type validation**: Use proper types to avoid conversion overhead

## 🤝 **Contributing**

Found a bug? Have a feature request? 

1. Check existing [issues](https://github.com/n8n-io/n8n-nodes-variables/issues)
2. Create detailed bug reports with workflow examples  
3. Submit pull requests with clear descriptions

## 📄 **License**

MIT - See [LICENSE.md](LICENSE.md) for details

## 🔗 **Links**

- [n8n Community](https://community.n8n.io/)
- [n8n Documentation](https://docs.n8n.io/)
- [Node Development Guide](https://docs.n8n.io/integrations/community-nodes/)

---

**Made with ❤️ for the n8n community**

*Transform your workflows with proper variable management!*
