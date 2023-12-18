namespace E_Commerce.Model
{
    public class Product
    {
        public int Id { get; set; }
        public string title { get; set; }
        public string description { get; set; }
        public decimal price { get; set; }
        public string category { get; set; }
        public int count { get; set; }
        public decimal rating { get; set; }

        public string image { get; set; }

    }
}
