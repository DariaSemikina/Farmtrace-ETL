CREATE TABLE IF NOT EXISTS `project_id`.`dataset`.`cows`
	(
    CowUNID string,
    Sex string,
    CowUNID_Father string,
    CowUNID_Mother string
	);


CREATE TABLE IF NOT EXISTS `project_id`.`dataset`.`cows_descendants`
	(
    CowUNID string,
    Descendants string,
    Depth int64
	);
