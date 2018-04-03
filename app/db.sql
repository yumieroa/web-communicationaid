--edit parent's info
create or replace function edit_parent( in par_efirstp text, in par_elastp text, in par_ebirthp date, in par_addp text) returns text as
$$
  declare
    loc_res text;

    loc_efirstp text;
    loc_elastp text;
    loc_ebirthp text;
    loc_addp text;
  begin
     select into loc_efirstp fname_p, loc_elastp lname_p, loc_ebirthp bday_p, loc_addp add_p from parent;
     if par_elastp NOTNULL then

       UPDATE parent SET (fname_p, lname_p, bday_p, add_p) = (par_efirstp,par_elastp,par_ebirthp,par_addp) where p_id='1';
       loc_res = 'ok';

     else
       loc_res = 'Error';
     end if;
     return loc_res;
  end;
$$
 language 'plpgsql';