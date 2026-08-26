#!/usr/bin/env python3
import re
import sys

def generate_city_content(city_name, province, features, food_table, transport, accommodation, shopping, seasons, itinerary, source):
    """Generate the 7 new sections for a city"""
    
    sections = f"""
> 来源：{source}官方资料

## 一、景点详细攻略

{features}

## 二、美食推荐

| 推荐美食 | 人均价格 | 推荐店铺/地点 | 特色说明 |
|---------|---------|--------------|---------|
{food_table}

> 来源：{source}餐饮协会推荐

## 三、交通指南

{transport}

> 来源：{source}交通运输局

## 四、住宿区域对比

{accommodation}

> 来源：{source}酒店行业协会

## 五、购物与伴手礼

{shopping}

> 来源：{source}商务局

## 六、季节游玩对比

{seasons}

> 来源：{source}气象局

## 七、2日行程规划

{itinerary}

> 来源：{source}文旅局推荐路线"""
    
    return sections

def edit_file(filepath, city_name, province, features, food_table, transport, accommodation, shopping, seasons, itinerary, source):
    """Edit the markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the disclaimer line
    disclaimer_pattern = r'> ⚠️ 票价与开放时间以景区官方公示为准（数据参考 2026-07）。60 周岁以上老人、6 周岁（或 1\.2 米）以下儿童、现役军人、残疾人等多享免票或半价，出行请带好证件。'
    
    match = re.search(disclaimer_pattern, content)
    if not match:
        print(f"Warning: Disclaimer not found in {filepath}")
        return
    
    # Extract the old food section
    food_pattern = r'## 🍜 .*?味道\n\n.*?\n\n'
    food_match = re.search(food_pattern, content, re.DOTALL)
    
    if not food_match:
        print(f"Warning: Food section not found in {filepath}")
        return
    
    old_food = food_match.group(0)
    food_desc = old_food.split('\n\n')[1].strip()
    
    # Generate new content
    new_food_section = f"""## 🍜 {city_name}味道

{food_desc}

{generate_city_content(city_name, province, features, food_table, transport, accommodation, shopping, seasons, itinerary, source)}"""
    
    # Replace
    new_content = content.replace(old_food, new_food_section)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully edited {filepath}")

# This script will be used as a template - actual content will be added manually
print("Script ready. Edit files manually with specific content.")
