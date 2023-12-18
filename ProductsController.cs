using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using E_Commerce.Model;

namespace E_Commerce.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductsController : ControllerBase
    {

        private static List<Product> Products = new List<Product>
        {
            new Product {
        Id = 1,
        title = "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        price = 109.95m,
        description = "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        category = "men's clothing",
        image = "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
        rating =  3.9m,
        count = 120

    },
            new Product {
        Id = 2,
        title = "Mens Casual Premium Slim Fit T-Shirts ",
        price =  22.3m,
        description =  "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
         category = "men's clothing",
        image = "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
        rating =  4.1m,
        count = 259

    }
 };

        private static int nextID = 1;

        [HttpGet]
        public IEnumerable<Product> Get()
        {
            return Products;
        }
        [HttpPost]

        public ActionResult<Product> Post(Product product)
        {
            if (product == null) return BadRequest();
            product.Id = nextID++;
            Products.Add(product);
            return CreatedAtAction(nameof(Get), new { id = product.Id }, Products);
        }

        [HttpPut("{id}")]
        public ActionResult Put(int id, Product product)
        {
            var index = Products.FindIndex(i => i.Id == id);
            if (index < 0) return NotFound();
            Products[index] = product;
            return NoContent();
        }

        [HttpDelete("{id}")]
        public ActionResult Delete(int id)
        {
            var index = Products.FindIndex(i => i.Id == id);
            if (index < 0) return NotFound();
            Products.RemoveAt(index);
            return NoContent();
        }

        public ActionResult<Product> Put(Product product)
        {
            if (product == null) return BadRequest();
            product.Id = nextID++;
            Products.Add(product);
            return CreatedAtAction(nameof(Get), new { id = product.Id }, Products);
        }
    }

}
