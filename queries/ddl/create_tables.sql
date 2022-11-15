CREATE TABLE IF NOT EXISTS `funda-bi-dev`.`dbt_darya_adhoc`.`cows`
	(
    CowUNID string,
    Sex string,
    CowUNID_Father string,
    CowUNID_Mother string
	);


CREATE TABLE IF NOT EXISTS `funda-bi-dev`.`dbt_darya_adhoc`.`cows_descendants`
	(
    CowUNID string,
    Descendants string,
    Depth int64
	);
