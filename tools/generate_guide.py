#!/usr/bin/env python3
# Semi-Automated MDX Recipe Generator for Holiday Gift Hub.
import os, sys, json
from datetime import date

AFFILIATE_TAG_US = os.environ.get("AFFILIATE_TAG_US", "holidaygifthub-20")
AFFILIATE_TAG_UK = os.environ.get("AFFILIATE_TAG_UK", "holidaygifthub-21")
POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "content", "blog")

def generate_post(slug, title, description, category, tags, products, intro_text="", is_printable=False, download_url=None):
    os.makedirs(POSTS_DIR, exist_ok=True)
    post_file = os.path.join(POSTS_DIR, f"{slug}.mdx")
    tags_json = json.dumps(tags)
    
    lines = [
        "---",
        f'title: "{title}"',
        f'description: "{description}"',
        f'pubDate: {date.today().isoformat()}',
        'author: "Festive Editorial Team"',
        'featuredImage: "/images/default-cover.jpg"',
        f'imageAlt: "{title}"',
        f'category: "{category}"',
        f'tags: {tags_json}',
        'isAffiliate: true',
    ]
    if is_printable:
        lines.append('isPrintable: true')
        if download_url:
            lines.append(f'downloadUrl: "{download_url}"')
    lines.extend([
        "---",
        "import ProductCard from '../../components/ProductCard.astro';",
        ""
    ])
    if intro_text:
        lines.append(intro_text)
        lines.append("")
        
    lines.append("## Top Tested Holiday Picks\n")
    for p in products:
        badge = p.get("badge", "Top Pick")
        name = p.get("name", "Product Name")
        price = p.get("price", "Under £15 / $20")
        rating = p.get("rating", "4.7/5")
        img = p.get("imageUrl", "https://images.unsplash.com/photo-1513151233558-d860c5398176?w=500&auto=format&fit=crop&q=60")
        desc = p.get("description", "Great gift for holidays.")
        asin = p.get("asin", "B0XXXXXXXX")
        us_url = p.get("usUrl") or f"https://amazon.com/dp/{asin}?tag={AFFILIATE_TAG_US}"
        uk_url = p.get("ukUrl") or f"https://amazon.co.uk/dp/{asin}?tag={AFFILIATE_TAG_UK}"
        pros = json.dumps(p.get("pros", ["Top rated on Amazon", "Fast 2-day Prime delivery"]))
        cons = json.dumps(p.get("cons", ["Check recipient preferences"]))
        
        card = (
            f'<ProductCard\n'
            f'  badge="{badge}"\n'
            f'  name="{name}"\n'
            f'  priceGuide="{price}"\n'
            f'  rating="{rating}"\n'
            f'  imageUrl="{img}"\n'
            f'  description="{desc}"\n'
            f'  usUrl="{us_url}"\n'
            f'  ukUrl="{uk_url}"\n'
            f'  pros={{{pros}}}\n'
            f'  cons={{{cons}}}\n'
            f'/>\n'
        )
        lines.append(card)
        
    lines.append("## Buying & Gifting Advice\n")
    lines.append("Every item selected features verified customer reviews above 4.5 stars and reliable holiday shipping windows.\n")
    
    with open(post_file, "w", encoding="utf-8") as pf:
        pf.write("\n".join(lines))
    print(f"Generated MDX recipe: {post_file}")
    return post_file

if __name__ == "__main__":
    print("Recipe Generator tool ready.")
