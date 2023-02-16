describe("Raises x to the power n", function(){
    it("5 ** 1 = 5", function() {
        assert.equal(pow(5, 1), 5);
    });
    it("5 ** 2 = 25", function() {
        assert.equal(pow(5, 2), 25);
    });
    it("5 ** 3 = 125", function() {
        assert.equal(pow(5, 3), 125);
    });
});