from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.country import Country

def generate_summary_image(db: Session):
    countries = db.query(Country).filter(Country.estimated_gdp != None).all()

    if not countries:
        return None

    total = len(countries)
    top5 = sorted(countries, key=lambda c: c.estimated_gdp or 0, reverse=True)[:5]

    # Create image (white background)
    img = Image.new("RGB", (900, 500), color="white")
    draw = ImageDraw.Draw(img)

    # Header
    draw.text((30, 30), "🌍 Country GDP Summary", fill="black", size=20)
    draw.text((30, 70), f"Total Countries: {total}", fill="black")
    draw.text((30, 100), f"Last Updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}", fill="black")

    # Table header
    y_offset = 160
    draw.text((30, y_offset), "Top 5 by Estimated GDP:", fill="black")
    y_offset += 40

    for c in top5:
        line = f"{c.name:<25} GDP: {round(c.estimated_gdp, 2):,.2f} | Pop: {c.population:,}"
        draw.text((50, y_offset), line, fill="black")
        y_offset += 30

    # Save image to file
    output_path = "summary.png"
    img.save(output_path)

    return output_path
