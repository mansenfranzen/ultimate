## Team Table

| team_id (pk, int) | name (char) | origin (char) | 
|-------------------|-------------|---------------| 
| 1                 | Heidees     | Heidelberg    | 
| 2                 | Gummis      | Karlsruhe     | 

## Tournament Table
| tour_id (pk, int) | name (char) | location (char) | start_time (datetime) | end_time (datetime) | type (int) | 
|-------------------|-------------|-----------------|-----------------------|---------------------|------------| 
| 1                 | Heidees Cup | Eppelheim       | 02.06.17              | 04.06.17            | 1          | 

## Game Table
| game_id (pk, int) | tour_id (fk) | timestamp          | type (int) | 
|-------------------|--------------|--------------------|------------| 
| 1                 | 1            | 02.06.2017 – 10:30 | 1          | 

## Game Score Table
| game_id (fk) | team_id (fk) | score (int) | 
|--------------|--------------|-------------| 
| 1            | 1            | 15          | 
| 1            | 2            | 10          | 

## Spirit Score Table
| score_id (pk) | game_id (fk) | subject (fk: team_id) | object (fk: team_id) | type (int) | value (int) | 
|---------------|--------------|-----------------------|----------------------|------------|-------------| 
| 1             | 1            | 1                     | 2                    | 1          | 4           | 
| 2             | 1            | 1                     | 2                    | 2          | 3           | 

## Account Table
| account_id (pk, int) | team_id (fk) | email (char)             | login (char) | type (int) | 
|----------------------|--------------|--------------------------|--------------|------------| 
| 1                    | 1            | pansen@franklinstoner.de | pansen       | 1          | 
| 2                    | 1            | brand.matthias@gmail.com | matze        | 1          | 
| 3                    | 1            | moritz.kretz@gmail.com   | mou          | 1          | 
| 4                    | 2            | irgendwer@karlsruhe.de   | Gummibär     | 2          | 

> Account Table may be redundant. Django Auth System should do the job. Team membership may be added directly to auth core table.

## Type Dictionary
| Tournament | Spirt Score   | Game     | Account        | 
|------------|---------------|----------|----------------| 
| Fun        | Kommunikation | Vorrunde | Admin          | 
| Reli       | Körperkontakt | Quarter  | Team Rechte    | 
| Nationals  | etc…          | Finale   | Turnier Rechte | 
| Europe     |               | etc…     |                | 
| etc…       |               |          |                | 

> Type choices may be hardcoded in the models.py?




