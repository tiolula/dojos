require 'rspec/autorun'
require_relative 'example_calculator'

describe "Sum calculation" do
    it "sums 1 and 2 and expect 3 as result" do
        entryA = 1
        entryB = 2
        expected = 3
        
        result = sum(entryA, entryB)

        expect(result).to eq(expected)
    end
end