create trigger product_update_trg after update on Product
begin
  update Product set updatedon = datetime('NOW') where ProductID = new.ProductID;
end;