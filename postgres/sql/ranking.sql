CREATE TABLE public.ranking (
	postcode varchar NOT NULL,
	profile_id int4 NOT NULL,
	"rank" float8 NULL,
	CONSTRAINT ranking_pkey PRIMARY KEY (postcode,profile_id)
);


-- public.ranking foreign keys

ALTER TABLE public.ranking ADD CONSTRAINT ranking_postcode_fkey FOREIGN KEY (postcode) REFERENCES public.postcode(postcode);
ALTER TABLE public.ranking ADD CONSTRAINT ranking_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profile(profile_id);