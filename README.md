# Pharmacy_Scrapping
The objective of this project is to get the product name, price, and link of the product from a pharmacy website.

⚠️ Disclaimer: The data got by the scraper was only used for practice purposes.
<br>
### Showing the data format got.
<img width="879" height="89" alt="image" src="https://github.com/user-attachments/assets/c9532eef-4f04-4f99-ba12-b3df718b4005" />

<br>

### CSV output
- When the function *format_csv_result* is executed to clean the data, this is the final result showing the products with their prices and if there is a discount price.
<img width="709" height="339" alt="image" src="https://github.com/user-attachments/assets/5347b39e-d6a6-4664-9dfd-91145a80838d" />

<br>

### Modify code
- To change the number of pages to visti, go to *pharmacy_scrapping.py* and change the next line:
```python
        #  Limit the number of pages to visit.
        'CLOSESPIDER_PAGECOUNT': 20
```

<br>

- To change  the starts_url
```python
'''
These URLs could be used in start_urls due to all having the same structure.:
- https://www.fahorro.com/farmacia.html
- https://www.fahorro.com/marca-del-ahorro.html
- https://www.fahorro.com/farmacia/marcas-destacadas.html
'''
start_urls = ['https://www.fahorro.com/vitaminas.html']
```
<br>

- Change download_delay time between 2 consecutive requests to the same domain.
```python
#  Decimal numbers are supported (2.5, 3.5)
download_delay = 5

```
<br>

- Also, the output format and where to store could be changed.
```python
process = CrawlerProcess({
     'FEED_FORMAT': 'csv',
     #  Format and where to save the file with the data extracted.
     'FEED_URI': 'Pharmacy/pharmacy_product.csv'
     })


```
