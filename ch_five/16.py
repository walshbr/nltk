# ◑ Explore the following issues that arise in connection with the lookup tagger:
# What happens to the tagger performance for the various model sizes when a backoff tagger is omitted?

"""i'd bet that it would perform better with lower sample sizes. because without a default tagging system, it would just have wide gaps with words that it had never seen before. no chance for hitting the words that it knew."""

# Consider the curve in 4.2; suggest a good size for a lookup tagger that balances memory and performance. Can you come up with scenarios where it would be preferable to minimize memory usage, or to maximize performance with no regard for memory usage?

"""if you're on a weak server or machine and need to minimize memory usage, sure. and ditto if you're in a situation in which POS tagging is hugely important."""