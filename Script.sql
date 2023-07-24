CREATE TABLE IF NOT EXISTS nanoisabello_coderhouse.movies
(
	title VARCHAR(256) NOT NULL  ENCODE lzo
	,"year release" VARCHAR(256)   ENCODE lzo
	,"type" VARCHAR(256)   ENCODE lzo
	,plot VARCHAR(256)   ENCODE lzo
	,imdbid VARCHAR(256)   ENCODE lzo
	,rated VARCHAR(256)   ENCODE lzo
	,released VARCHAR(256)   ENCODE lzo
	,runtime VARCHAR(256)   ENCODE lzo
	,genre VARCHAR(256)   ENCODE lzo
	,director VARCHAR(256)   ENCODE lzo
	,writer VARCHAR(256)   ENCODE lzo
	,actors VARCHAR(256)   ENCODE lzo
	,"language" VARCHAR(256)   ENCODE lzo
	,country VARCHAR(256)   ENCODE lzo
	,awards VARCHAR(256)   ENCODE lzo
	,poster VARCHAR(256)   ENCODE lzo
	,ratings VARCHAR(256)   ENCODE lzo
	,metascore VARCHAR(256)   ENCODE lzo
	,imdbrating VARCHAR(256)   ENCODE lzo
	,imdbvotes VARCHAR(256)   ENCODE lzo
	,dvd VARCHAR(256)   ENCODE lzo
	,boxoffice VARCHAR(256)   ENCODE lzo
	,production VARCHAR(256)   ENCODE lzo
	,website VARCHAR(256)   ENCODE lzo
	,response VARCHAR(256)   ENCODE lzo
)
DISTSTYLE AUTO
;
ALTER TABLE nanoisabello_coderhouse.movies owner to nanoisabello_coderhouse;