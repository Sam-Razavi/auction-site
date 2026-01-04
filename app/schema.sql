DROP TABLE IF EXISTS auctions;
DROP TABLE IF EXISTS bids;
DROP TABLE IF EXISTS reactions;

CREATE TABLE auctions (
    id INTEGER PRIMARY KEY ,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    starting_bid INTEGER NOT NULL,
    end_datetime TEXT NOT NULL
);

CREATE TABLE bids (
    id INTEGER PRIMARY KEY ,
    auction_id INTEGER NOT NULL,
    bidder_email TEXT NOT NULL,
    bid_amount INTEGER NOT NULL,
    bid_datetime TEXT NOT NULL,
    FOREIGN KEY (auction_id) REFERENCES auctions (id)
);

CREATE TABLE reactions (
    id INTEGER PRIMARY KEY ,
    auction_id INTEGER NOT NULL,
    reaction_type TEXT NOT NULL, -- 'like' or 'dislike'
    created_at TEXT NOT NULL,
    FOREIGN KEY (auction_id) REFERENCES auctions (id)
);
