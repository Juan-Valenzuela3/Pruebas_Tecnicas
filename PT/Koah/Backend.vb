// Entity Product
public class Product
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Sku { get; set; } // único
    public decimal Price { get; set; }
    public int Stock { get; set; }
    public string Category { get; set; }
}

// DbContext y Migración inicial
public class AppDbContext : DbContext
{
    public DbSet<Product> Products { get; set; }
    protected override void OnConfiguring(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Product>()
            .HasIndex(p => p.Sku)
            .IsUnique();
    }
}

// Comandos para ejecutar migración inicial
    // dotnet ef migrations add InitialCreate
    // dotnet ef database update

// Cargar 5 productos de ejemplo
public static class DbInitializer
{
    public static void Initialize(AppDbContext context)
    {
        if (context.Products.Any())
        {
            context.Products.AddRange(
                new Product { Name = "Laptop", Sku = "LAP123", Price = 999.99M, Stock = 10, Category = "Electronics" },
                new Product { Name = "Smartphone", Sku = "SMP456", Price = 499.99M, Stock = 25, Category = "Electronics" },
                new Product { Name = "Desk Chair", Sku = "CHR789", Price = 89.99M, Stock = 15, Category = "Furniture" },
                new Product { Name = "Notebook", Sku = "NTB101", Price = 2.99M, Stock = 100, Category = "Stationery" },
                new Product { Name = "Pen", Sku = "PEN202", Price = 0.99M, Stock = 200, Category = "Stationery" }
            );
            context.SaveChanges();
        }
    }
}
    
// Endpoints (Controller)

[ApiController]
[Route("api/products")]
public class ProductsController : ControllerBase
{
    private readonly AppDbContext _context;
    public ProductsController(AppDbContext context) => _context = context;

    [HttpGet]
    public IActionResult GetAllProducts(string search = null)
    {
        var products = _context.Products.ToList();
        return Ok(products);
    }

    [HttpGet("{id}")]
    public IActionResult GetProduct(int id)
    {
        var product = _context.Products.Find(id);
        if (product == null) return NotFound();
        return Ok(product);
    }

    [HttpPost]
    public IActionResult CreateProduct(Product product)
    {
        if (_context.Products.Any(p => p.Sku == product.Sku))
            return Conflict("SKU must be unique.");

        _context.Products.Add(product);
        _context.SaveChanges();
        return CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product);
    }

    [HttpPut("{id}")]
    public IActionResult UpdateProduct(int id, Product updatedProduct)
    {
        var product = _context.Products.Find(id);
        if (product == null) return NotFound();

        product.Name = updatedProduct.Name;
        product.Price = updatedProduct.Price;
        product.Stock = updatedProduct.Stock;
        product.Category = updatedProduct.Category;
        // SKU no se actualiza
        _context.SaveChanges();
        return NoContent();
    }
}

// Configuración de Swagger en Startup.cs
   // services.AddSwaggerGen();
    // app.UseSwagger();
    // app.UseSwaggerUI();
