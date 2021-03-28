# Elastic Cloud

This week, you will learn about Elastic Cloud, a platform which enables search and analytics for both structured and non-structured data.

If you want to broaden your knowledge beyond this lab, the Elastic website provides many [video tutorials](https://www.elastic.co/videos/).

## Goals

* Become aware of the various components of the Elastic stack and their respective roles
* Explore the Kibana visualization tools
* Get acquainted with the Query DSL search syntax

## Lab Structure

**Hour 1**:

1. Questions about last week's lab?
2. Questions about the project?
3. Elastic Cloud walkthrough
4. Exercise: Create a deployment

**Hour 2**:

5. Kibana walkthrough
6. Exercise: Upload log data to Elastic (for the personal assignment)
7. Query DSL demo

In case we finish the lab earlier, students can use the remaining time to work on their project.

## Walkthroughs

### Elastic Cloud

* The Elastic stack: Logstash and Beats (data ingest), Elasticsearch (storage, indexing, querying), and Kibana (dashboard)
* A managed cloud platform based on open-source software
* *Elasticsearch-as-a-Service*
* Create a deployment (aka cluster)
* Elastic documentation

### Dashboard

* Explore the sample data: eCommerce orders & web logs
* Kibana tools: Discover, Dashboard, Canvas, Maps, Graph
* Upload custom data
* Dev Tools and the Query DSL (demo of `match`, `bool`, `range`, and `aggs` queries)

If you are unsure how to make your queries, the [Query DSL documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) has everything, including examples.

With the `elasticsearch-dsl` package, it is possible to query your data with Python (see notebook in this folder). Try it at home!
