

from contextlib import closing
import datetime
import os
import sqlite3

import librivox


OUTPUT_DIR = './output'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
TIME_OUTPUT = '%Y%m%d-%H%M%S'


def main():
    os.makedirs(OUTPUT_DIR)
    with sqlite3.connect(librivox.LIBRIVOX_DB) as cxn:
        with closing(cxn.cursor()) as c:
            c.execute('''
                SELECT id, text, scraped
                FROM postings
                ORDER BY scraped;
                ''')
            for (post_id, text, scraped_str) in c:
                scraped = datetime.datetime.strptime(scraped_str, TIME_FORMAT)
                output = os.path.join(
                    OUTPUT_DIR,
                    '%06d-%s.txt' % (post_id, scraped.strftime(TIME_OUTPUT)),
                    )
                with open(output, 'w') as f:
                    f.write(text)


if __name__ == '__main__':
    main()
