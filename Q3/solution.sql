SELECT owner.owner_id, owner.owner_name, COUNT(*) AS different_category_count
FROM owner, article, category_article_mapping, category 
WHERE owner.owner_id = article.owner_id, article.article_id = category_article_mapping.article_id, category_article_mapping.category_id = category.category_id
GROUP BY owner.owner_id
