using Microsoft.EntityFrameworkCore;
using PT_Backend.Models;

namespace PT_Backend.Models
{
    public class Product
    {
        public int Id { get; set; }
        public string Sku { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
        public int Stock { get; set; }
        public string Category { get; set; }
    }

    }

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<Product> Products { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Product>()
            .HasIndex(p => p.Sku)
            .IsUnique();

        // Datos iniciales
        modelBuilder.Entity<Product>().HasData(
            new Product { Id = 1, Name = "Laptop", Sku = "LAP123", Price = 999.99M, Stock = 10, Category = "Electronics" },
            new Product { Id = 2, Name = "Smartphone", Sku = "SMP456", Price = 499.99M, Stock = 25, Category = "Electronics" },
            new Product { Id = 3, Name = "Desk Chair", Sku = "CHR789", Price = 89.99M, Stock = 15, Category = "Furniture" },
            new Product { Id = 4, Name = "Notebook", Sku = "NTB101", Price = 2.99M, Stock = 100, Category = "Stationery" },
            new Product { Id = 5, Name = "Pen", Sku = "PEN202", Price = 0.99M, Stock = 200, Category = "Stationery" }
        );
    }
}


