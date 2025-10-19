using Microsoft.AspNetCore.Mvc;
using System.Linq;
using PT_Backend.Models; 


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
