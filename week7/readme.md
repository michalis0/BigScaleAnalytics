# Elasticsearch: Part 2

_The lab will start at 2.15pm._

This week, we will see how to leverage Elasticsearch's "Edge n-gram" tokenizer to create an autocompletion functionality and thus enhance the search experience. Students will also spend time building a dashboard.

## Goals

* Learn how autocompletion works in Elasticsearch
* Experiment with the dashboard functionalities

## Lab Structure

1. Questions about the assignment?
2. Questions about milestone 2 of the project?
3. Autocompletion in Elasticsearch
4. Exercise: Creating a Kibana dashboard

Students can use the remainder of the afternoon to finish their deliverable for milestone 2.

## Walkthroughs

### Autocompletion in Elasticsearch

Autocompletion is also known as "incremental search" or "search-as-you-type". Here are two approaches you can implement this in Elasticsearch:

* The simple, suboptimal approach: **`prefix` queries**
* The advanced, more powerful approach: **Edge n-grams**

## Exercises

### Creating a Kibana dashboard

1. Find a public dataset (e.g., on Kaggle, data.world, etc.)
2. Add and index the data on Elasticsearch (_Home_ > _Upload a file_)
3. Think of a use case: what knowledge do you want to extract from the data?
3. Create a new dashboard (_Analytics_ > _Dashboard_ > _Create dashboard_)
4. Add three panels that are relevant to your use case. Try using different types of panels!
5. Present your dashboard to the class: which dataset, which visualizations you chose and why.
