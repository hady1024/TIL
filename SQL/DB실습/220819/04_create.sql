-- 1. 모든 테이블의 이름을 출력하세요.
.table
-- table
----------------------
-- albums          employees       invoices        playlists
-- artists         genres          media_types     tracks
-- customers       invoice_items   playlist_track

-- 2. 모든 테이블의 데이터를 확인해보세요.

-- | 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.

-- 3. 앨범(albums) 테이블의 데이터를 출력하세요.

-- | 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.
SELECT * FROM albums GROUP BY Title ORDER BY Title DESC LIMIT 5; 
-- albumid   Title                          artistid
-- -------  --------                        ---------
-- 208      [1997] Black Light Syndrome     136
-- 240      Zooropa                         150
-- 267      Worlds                          202
-- 334      Weill: The Seven Deadly Sins    264
-- 8        Warner 25 Anos                   6

-- 4. 고객(customers) 테이블의 행 개수를 출력하세요.
SELECT COUNT(*) "고객 수" FROM customers;
-- 고객수
-- 59