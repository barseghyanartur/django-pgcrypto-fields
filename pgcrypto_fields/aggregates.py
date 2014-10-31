from django.db import models

from pgcrypto_fields.sql import aggregates


class Decrypt(models.Aggregate):
    """`Decrypt` creates an alias for `DecryptFunctionSQL`.

    `alias` is `{self.lookup}__decrypt` where 'decrypt' is `self.name.lower()`.

    `self.lookup` is defined in `models.Aggregate.__init__`.
    """

    def add_to_query(self, query, alias, col, source, is_summary):
        """Add the aggregate to the query."""
        klass = getattr(aggregates, self.name)
        aggregate = klass(
            col,
            source=source,
            is_summary=is_summary,
            **self.extra
        )
        query.aggregates[alias] = aggregate
