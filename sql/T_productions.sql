create table productions(
prod_id int AUTO_INCREMENT primary key,
description text not null,
is_active int default 1,
create_dt datetime
);


insert into productions(description, create_dt)
values('The Nutcracker 2019',  date(NOW()));

insert into productions(description, create_dt)
values('Across The Pond',  date(NOW()));

insert into productions(description, create_dt)
values('Academy 2019 Summer Showcase',  date(NOW()));

insert into productions(description, create_dt)
values('Jane the most Eyre',  date(NOW()));

insert into productions(description, create_dt)
values('The Nutcracker 2020',  date(NOW()));

insert into productions(description, create_dt)
values('The Nutcracker 2021',  date(NOW()));