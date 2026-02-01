# n8n-nodes-centum

![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

This is a custom node for [n8n](https://n8n.io/), an open-source workflow automation platform, designed to integrate with the **Centum API**, a system for managing customers, payments, and other business resources.  
The `Centum` node simplifies interaction with the Centum API endpoints, allowing operations such as customer search, payment creation, and more directly inside your n8n workflows.

The node is built to be extensible, making it easy to add new operations for specific integration needs with Centum.

## Requires 3 parameters in the **Centum API** credential:

| Field                             | Type       | Example                                                     | Required |
|-----------------------------------|------------|-------------------------------------------------------------|----------|
| Public Access Key                 | Password   | a1b2c3d4e5f6g7h8i9j0...                                     | Yes      |
| CentumSuiteConsumidorApiPublicaId | Number     | 12345                                                       | Yes      |
| Centum URL                        | Text (URL) | https://plataformaX.centum.com.ar:23990/BLX                 | Yes      |
|-----------------------------------|------------|-------------------------------------------------------------|----------|



## Available Operations

**42 endpoints organized into 5 categories:**

### 📦 Articles
- `articulo`: Search articles with filters (categories, dates, stock)
- `articuloPorId`: Query by exact ID or code
- `articulosDatosGenerales`: Retrieve general article data
- `articulosExistencia`: Stock availability by branch
- `articulosImagenes`: Download and process article images
- `articulosPrecioPorLista`: Prices by price list
- `articulosSucursalesFisicas`: Articles grouped by branch
- `articuloSucursalFisica`: Specific article in branch
- `categoriasObtener`: List categories
- `marcasObtener`: List brands
- `rubrosObtener`: List product groups

### 👤 Customers
- `clienteNuevo`: Create a new customer
- `nuevoContribuyente`: Register a taxpayer with CUIT
- `clientes`: Paginated customer list
- `clientesActualizar`: Update customer data
- `clientesBusqueda`: Search by email or DNI
- `clientesBusquedaPorCuit`: Search by CUIT
- `buscarContribuyente`: Search taxpayer
- `composicionSaldoCliente`: Detailed account status
- `obtenerSaldoCliente`: Current account balance

### 💳 Orders and Payments
- `cobros`: Register a payment
- `obtenerCobros`: Filter payments
- `obtenerFacturasCobros`: Payment invoice history
- `crearPedidoVenta`: Create a sales order
- `obtenerPedidosDeVenta`: List sales orders
- `obtenerFacturasPedidosVentas`: Sales order invoice history
- `obtenerEstadosPedidosDeVenta`: Available sales order statuses
- `pedidoVentaActividad`: Check sales order activity
- `generarVentas`: Generate a sale
- `generarCompras`: Generate a purchase
- `obtenerCompras`: Filter purchases

### 🌍 Catalogs
- `provinciasLista`: List of provinces (Argentina)
- `departamentosLista`: Departments by province
- `sucursalesFisicas`: Physical branches
- `listaPrecios`: Available price lists
- `promocionesCliente`: Commercial promotions for customers
- `regimenesEspecialesLista`: Special tax regimes
- `regimenesEspecialesPorId`: Special regime by ID
- `tipoComprobante`: Voucher types

### ⚙️ Utilities
- `generarProductosWoo`: Transform data to WooCommerce format
- `procesarImagenes`: Image processing and synchronization
- `generarToken`: Authentication token generation
- `operadoresMoviles`: Retrieve mobile operator data based on credentials

## Prerequisites

To use this node, make sure you have the following installed in your development environment:

- **n8n**: Version 1.75.2 or higher (latest recommended for compatibility).
- **Node.js**: Version 20.x or higher.
- **npm**: Required to install and build the plugin.
- **Git**: To clone the repository.
- **Centum API access**: Valid credentials (`centumUrl`, `consumerApiPublicId`, `publicAccessKey`) provided by your Centum provider.

Recommended: Follow the n8n guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Using this Starter

Basic steps to work with this starter. For a detailed guide on creating and publishing nodes, see the [documentation](https://docs.n8n.io/integrations/creating-nodes/).

1.  [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate) from this template.
2.  `git clone https://github.com/<your-username>/<your-repo>.git`
3.  Run `npm i` to install dependencies.
4.  Open the project in your editor.
5.  Explore the examples in `/nodes` and `/credentials`. Modify or replace them with your own nodes.
6.  Update `package.json` with your details.
7.  Run `npm run lint` to check for errors or `npm run lintfix` to fix them automatically.
8.  Test your node locally. See [Running your node locally](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/).
9.  Replace this README with your node documentation. Use the [README TEMPLATE](/broobe/n8n/n8n-nodes-blocky-nodes/-/blob/main/README_TEMPLATE.md) as a base.
10. Update the LICENSE file with your details.
11. [Publish](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry) your package to npm.

## Support

For issues or questions:
- Open an **issue** in the [GitHub repository](https://github.com/your-username/n8n-nodes-centum).
- Contact your Centum provider for API-related support.
- Check the [n8n documentation](https://docs.n8n.io/) for help with workflow integration.

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.
